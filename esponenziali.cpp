#include <iostream>
#include <cmath>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

int main() {
	srand(time(NULL));
	
	ofstream dati0("logica.txt");
	ofstream dati1("guariti.txt");
	ofstream dati2("morte.txt");
	ofstream dati3("contagi.txt");
	ofstream espo("esponenziale.txt");
	
	ofstream dati("giorni.txt");
	
	unsigned long long int gua; //guarigione
	unsigned long long int g[100000];
	unsigned long long int pop; //popolazione
	unsigned long long int i = 0;
	unsigned long long int e = 1;
	unsigned long long int log = 1; //dati curva logica
	unsigned long long int tm; // tasso di morte
	unsigned long long int pg = 0; //persone guarite
	unsigned long long int con = 0; //contagiati
	float econ = 1;
	double gio=1;
	int giorni = gio;
	cout<<"inserisci tasso di morte[0-100]: "; cin>>tm;
	cout<<"inserisci giorni per guarire: "; cin>>gua;
	cout<<"inserisci popolazione: "; cin>>pop;
	
	system("cls");
	g[0]=1;
	dati0<<pop<<endl;
	dati1<<pop<<endl;
	dati2<<tm<<endl;
	dati3<<pop<<endl;
	espo<<pop<<endl;
	
	float a;
	pop = pop + 1;
	unsigned long long int p = pop;
	unsigned long long int po = pop/100;
	
	while(e <= p) {
		Sleep(100);
		
		if(e<p) {
			con = e;
		}
		if(giorni>=gua) {
			con = con - g[i];
			p = p - g[i];
			pg = pg + g[i];
			i++;
		}
		if(econ<po) {
			econ=(1+0.21)*econ;
			if(econ>po) econ = po;
			espo<<econ<<endl;
		}
		a = pow(2.718,-1*0.21*gio);
		e = p/(1+(p-1)*a);
		log = pop/(1+(pop-1)*a);
		g[giorni] = e - con;
		cout<<"Giorno"<<giorni<<endl<<"Contagiati: "<<con<<endl<<"Guariti+morti totali:"<<pg<<endl<<endl;
		dati<<"Giorno"<<giorni<<endl<<"Contagiati: "<<con<<endl<<"Guariti+morti totali:"<<pg<<endl<<endl;
		dati0<<log<<endl;
		dati1<<pg<<endl;
		dati3<<con<<endl;
		giorni++;
		gio++;
		if(con == 0) break;
	}
	dati0.close();
	dati1.close();
	dati2.close();
	dati3.close();
	fflush(stdin);getchar();
	system("start esponenziali.py");
	return 0;
}
