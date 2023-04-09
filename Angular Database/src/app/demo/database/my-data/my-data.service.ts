import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MyDataTable } from './my-data';
import { shareReplay } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyDataService {

  getData$ = this.getData().pipe(
    shareReplay(1)
  );

  constructor(private http: HttpClient) { }

  getData() {
    return this.http.get<MyDataTable[]>('https://jsonplaceholder.typicode.com/comments');
  }
}
