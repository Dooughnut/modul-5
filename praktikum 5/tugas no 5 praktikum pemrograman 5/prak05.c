#include <stdio.h>
void Biodata(int tahunLahir, char Namaku[30] ,char Asal[15]){
int tahun_sekarang = 2020;
int umur = tahun_sekarang - tahunLahir; 
printf("Perkenalkan Nama Saya :%s \n",Namaku);
printf("umur saya: %d\n",umur);
printf("saya adalah angkatan: %d\n",tahun_sekarang);
printf("asal saya dari: %s",Asal);
}

int main() {
int tahunLahir;
char A[20], B[15];
scanf(" %d",&tahunLahir);
scanf(" %[^\n]%*c",&A);
scanf(" %[^\n]%*c",&B);
Biodata(tahunLahir, A, B);
return 0;
}
 