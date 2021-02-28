/***
* KNAPSACK - The Knapsack Problem no tags
* The famous knapsack problem. You are packing for a vacation
* on the sea side and you are going to carry only one bag with
* capacity S (1 <= S <= 2000). You also have N (1<= N <= 2000)
* items that you might want to take with you to the sea side.
*  Unfortunately you can not fit all of them in the knapsack so
* you will have to choose. For each item you are given its size and its value.
* You want to maximize the total value of all the items you are going to bring.
* What is this maximum total value?
*
* Input
* On the first line you are given S and N.
* N lines follow with two integers on each line describing one of your items.
* The first number is the size of the item and the next is the value of the item.
*
* Output
* You should output a single integer on one like - the total maximum value from the
* best choice of items for your trip.
*
* Example
*
* Input:
* 4 5
* 1 8
* 2 4
* 3 0
* 2 5
* 2 3
*
*
* Output:
* 13
* Submit solution!
***/


#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define MAX_TODO 2005


long valor[MAX_TODO], tamanio[MAX_TODO], memo[MAX_TODO][MAX_TODO],capacidad_mochila,cantidad_items;


long mochila(int id, int capacidad) {
  if (capacidad< 0){ return -999999999;}
  if(capacidad == 0 || id >= cantidad_items){return 0;}
  if(memo[id][capacidad] != 0){return memo[id][capacidad];}
  else{return memo[id][capacidad] = max(mochila(id + 1,capacidad-tamanio[id]) + valor[id],mochila(id + 1,capacidad));}
}

int main(int argc, char const *argv[]) {
  //ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  scanf("%ld %ld",&capacidad_mochila,&cantidad_items);
  for (int i = 0; i < cantidad_items; i++) {
      scanf("%ld %ld",&tamanio[i],&valor[i]);
  }
  //long res  = mochila(0,capacidad_mochila);

  printf("%ld\n",mochila(0,capacidad_mochila));
  return 0;
}
