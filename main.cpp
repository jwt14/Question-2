//  HPC_Q2
//
//  Created by Jan Witold Tomaszewski CID: 00833865.
#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <limits>
#include <fstream>
#include <iterator>
#include "TriMatrix.h"
#define _USE_MATH_DEFINES
using namespace std;

/*----------------------------- Generating Identity and Tridiagonal Spatial Matrices using help functions ------------------------------------------------------------*/
TriMatrix MakeIdentityMatrix(int N_x){
     TriMatrix Identity(N_x+2);
     for (int i=2; i <=N_x;i++){
                    Identity(i,i) = 1;
                    Identity(i,i-1) = 0;
                    Identity(i,i+1) = 0;
    }
    Identity(1,1) = 1;
    Identity(N_x+1,N_x+1) = 1;
    Identity(1,2) = 0;
    Identity(N_x+1,N_x) = 0;
    return Identity;
}

TriMatrix MakeSpatialOpMatrix(int N_x){
     TriMatrix Spatial(N_x+2);
     for (int i=2; i <=N_x;i++){
                    Spatial(i,i) = -2;
                    Spatial(i,i-1) = 1;
                    Spatial(i,i+1) = 1;
    }
    Spatial(1,1) = 0;
    Spatial(N_x+1,N_x+1) = 0;
    Spatial(1,2) = 0;
    Spatial(N_x+1,N_x) = 0;

    return Spatial;
}

 /*----------------------------- Printing and input-validating functions for both doubles and integers ----------------------------------------------------------------*/
void print_vector(vector<double> U){
    int m = U.size();
    cout << "The solution is:" << endl;                           //Each solution is printed to a terminal
    for (int i=0;i<m;++i){
        cout << U[i] << endl;
    }
}

void validating(double &vIn){
    while(1){
        if(cin.fail() || vIn <= 0){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout<<"You have entered wrong input"<<endl;
            cin>>vIn;
        }
    if(!cin.fail())
        break;
    }
}

void validating(int &vIn){
    while(1){
        if(cin.fail() || vIn <= 0){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout<<"You have entered wrong input"<<endl;
            cin>>vIn;
        }
    if(!cin.fail())
        break;
    }
}


int main(int argc, char* argv[]) {
    /*----------------------------- Program description ---------------------------------------------------------------------------------------------------------------*/
    //
    //  This is HPC Q2 solution. It provides a solution to a heat equation problem in a form of a temerature vectors.
    //  Major changes: Removed user-input, changed heat distribution into sinusoid, removed vector printing to an external txt file.
    //
    /*----------------------------- Declaring variables and prompting for input with validation -----------------------------------------------------------------------*/

	double L=atof(argv[1]);
	int N_x=atoi(argv[2]);
	double T=atof(argv[3]);
	int N_t=atoi(argv[4]);
	double alpha=atof(argv[5]);                                                         //removed cin commends and specified 5 input arguments      !!!
    double del_x = L/(double(N_x));
    double del_t = T/(double(N_t));

    double nu = alpha*(del_t/pow(del_x,2));                                             //calculating Courant number

    /*----------------------------- Generating vectors with initial conditions ----------------------------------------------------------------------------------------*/
    vector<double> u_0, u, u_CN;                                                                //u_0 stores initial heat distribution;
    for(int j=0; j<N_x+1; j++){                                                                 //u stores heat at next full time step;
        u_0.push_back(sin(M_PI*j*del_x/L));                                                     //changed to sinusoid heat distribution
     }

    /*----------------------------- Generating Identity and Spatial triMatrices using help functions ------------------------------------------------------------------*/
    TriMatrix I(N_x+2);
    TriMatrix l(N_x+2);
    TriMatrix A(N_x+2);

    l = MakeSpatialOpMatrix(N_x);                                                       //Lowercase l as uppercase is reserved for bar length!
    I = MakeIdentityMatrix(N_x);
    A = I+l*nu;                                                                         //Generating A matrix with (v, 1-2v, v)


    for(double k=0;k<N_t;++k){
        u = A * u_0;                                                                    //Implementing for loop with an overloaded vector-matrix multiplication
        u_0 = u;
        print_vector(u);                                                               //Printing vector after each loop to be captured by Python      !!!
    }
    return 0;
}
