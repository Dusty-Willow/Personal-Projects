import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Resolve, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { Employee } from '../employees/employees';
import { EmployeeService } from '../employees/employees.service';

@Injectable({
  providedIn: 'root'
})
export class EmployeeGuard implements Resolve<Employee[]> {
  
  constructor (private myEmployeesService: EmployeeService) {}
  
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Employee[] | Observable<Employee[]> | Promise<Employee[]> {
      return this.myEmployeesService.getEmployees();
  }
}
