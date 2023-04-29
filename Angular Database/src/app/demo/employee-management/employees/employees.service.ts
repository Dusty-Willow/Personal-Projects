import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map, shareReplay } from 'rxjs';
import { Employee } from './employees';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

    // private _employeesJsonURL = '/assets/databases/employee.database.json'
    private _employeesJsonURL = 'http://localhost:3000/Employees'
    // private _departmentsJsonURL = '/assets/databases/department.database.json'

    // getEmployees$ = this.getEmployees().pipe(
    // shareReplay(1)
    // );

    constructor(private http: HttpClient) { }

    fetchData() {
      return this.getEmployees().pipe(
        shareReplay(1)
      );
    }

    getEmployees() {
      return this.http.get<Employee[]>(this._employeesJsonURL);
    }

    addEmployee(employee: any) {
      return this.http.post(this._employeesJsonURL, employee);
    }

    deleteEmployee(id: number): Observable<Employee[]> {
      const url = `${this._employeesJsonURL}/${id}`;
      console.log(url);
      return this.http.delete<Employee[]>(url);
    }

    isolateEmployee(id: number) {
      const url = `${this._employeesJsonURL}/${id}`;
      return this.http.get<Employee>(url).pipe(shareReplay(1));
    }

    updateEmployee(id: number, employee: any) {
      const url = `${this._employeesJsonURL}/${id}`;
      return this.http.put(url, employee);
    }
}
