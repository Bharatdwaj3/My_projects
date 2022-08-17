#include<iostream>
using namespace std;
class Bank_customer
{
	char name[50];
	char acc_t[50];
	int acc_no;
	float age;
	public : void getdata(void);
			 void putdata(void);
};
void Bank_customer::getdata()
{
	cout<<"Enter name : ";
	cin>>name;
	cout<<"Enter age : ";
	cin>>age;
	cout<<"Account number : ";
	cin>>acc_no;
	cout<<"Account type : ";
	cin>>acc_t;
}
void Bank_customer::putdata()
{
	cout<<"Name : "<<name<<"\n";
	cout<<"Age : "<<age<<"\n";
	cout<<"Account Number : "<<acc_no<<"\n";
	cout<<"Account Type : "<<acc_t<<"\n";
}
const int size=10;
int main()
{
	int i;
	Bank_customer acc_info[size];
	for(int i=0;i<size;i++)
	{
		cout<<"\n Details of the Bank Account Holder "<<i+1<<"\n";
		acc_info[i].getdata();
	}
	cout<<"\n";
	for(i=0;i<size;i++)
	{
		cout<<"\n Bank Account Holder"<<i+1<<"\n";
		acc_info[i].putdata();
	}
	cout<<"\n ";
       return 0;
}