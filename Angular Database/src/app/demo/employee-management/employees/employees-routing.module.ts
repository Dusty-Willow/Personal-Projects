import { NgModule } from '@angular/core';
import { EmployeesComponent } from './employees.component';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeGuard } from '../guards/employees.guard';
import { EmployeeAddComponent } from '../employee-add/employee-add.component';
import { EmployeeEditComponent } from '../employee-edit/employee-edit/employee-edit.component';

const routes: Routes = [
  { path: '', component: EmployeesComponent, resolve: {myEmployees: EmployeeGuard}},
  { path: 'add', component: EmployeeAddComponent },
  { path: 'edit/:id', component: EmployeeEditComponent }
]

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeesRoutingModule { }
