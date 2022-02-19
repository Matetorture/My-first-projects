#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

int losowa;
int wylosowana;
int zgadywana;
int przedzial;
bool a;

int main() {
  a=true;
  
  cout<<"Odgadnij Liczbę."<<endl<<endl;
  cout<<"Z jakiego przedziału ma losować liczbę?"<<endl;
  cout<<"od 1 do ";
  cin>>przedzial;
  cout<<endl;

  srand(time(NULL));
  losowa=rand();
  wylosowana=losowa%przedzial+1;
  
  while(a==true)
    {
      cout<<endl;
      cout<<"Zgadnij Liczbę: ";
      cin>>zgadywana;
      
      if(zgadywana==wylosowana)
      {
        cout<<"Brawo! Zgadłeś.";
        a=false;
      }
      if(zgadywana<wylosowana)
      {
        cout<<"Więcej niż "<<zgadywana<<"."<<endl;
      }
      if(zgadywana>wylosowana)
      {
        cout<<"Mniej niż "<<zgadywana<<"."<<endl;
      }
    }
}