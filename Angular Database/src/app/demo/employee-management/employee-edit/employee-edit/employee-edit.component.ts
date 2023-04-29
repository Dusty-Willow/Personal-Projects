import { Component, OnInit } from '@angular/core';
import { EmployeeService } from '../../employees/employees.service';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Employee } from '../../employees/employees';

@Component({
  selector: 'app-employee-edit',
  templateUrl: './employee-edit.component.html',
  styleUrls: ['./employee-edit.component.scss']
})
export class EmployeeEditComponent implements OnInit {

  editable: boolean = false;
  currentEmployee = Number(this.router.url.split('/').pop());



  employee = {
    id: this.currentEmployee
  }

  successMessage: string = "";

  constructor(private employeeService: EmployeeService, private router: Router) { }

  ngOnInit(): void {
      
  }

  updateEmployee(employeeForm: NgForm) {
    this.employeeService.addEmployee(this.employee).subscribe((data) => {
      this.successMessage = 'Employee Added to Database.';
    })
    console.log(this.employee)
  }

}
