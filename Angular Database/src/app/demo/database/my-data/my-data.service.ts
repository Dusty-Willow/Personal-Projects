import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MyData } from './my-data';

@Injectable({
  providedIn: 'root'
})
export class MyDataService {

  constructor(private http: HttpClient) { }

  getData() {
    return this.http.get<MyData[]>('https://jsonplaceholder.typicode.com/comments');
  }
}
