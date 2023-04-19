import { NgModule } from '@angular/core';
import { EmployeesComponent } from './employees.component';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeGuard } from '../guards/employees.guard';

const routes: Routes = [{ path: '', component: EmployeesComponent, resolve: {myEmployees: EmployeeGuard}}]

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeesRoutingModule { }