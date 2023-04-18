import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { shareReplay } from 'rxjs';
import { Employee } from './employees';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

    private _employeesJsonURL = '/assets/databases/employee.database.json'
    // private _departmentsJsonURL = '/assets/databases/department.database.json'

    getEmployees$ = this.getEmployees().pipe(
    shareReplay(1)
    );


    // getDepartments$ = this.getDepartments().pipe(
    // shareReplay(1)
    // );

    constructor(private http: HttpClient) { }

    getEmployees() {
        return this.http.get<Employee[]>(this._employeesJsonURL);
    }

    // getDepartments() {
    //     return this.http.get<Department[]>(this._departmentsJsonURL);
    // }
}
