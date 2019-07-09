#include <stdio.h>

int centrage(int k);

int main(int argc, char *argv[]) {
	int size = 10;
	int i, j;
	for (i = 0; i < size; i++) {
		centrage(size - 1 - i);
		for (j = 0; j < i; j++) {
			printf("*");
		}
		for (j = 0; j < i - 1; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}

int centrage(int k) {
	int i;
	for (i = 0; i < k; i++)
		printf("%c", ' ');
	return 0;	
}