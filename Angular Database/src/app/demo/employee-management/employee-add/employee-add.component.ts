import { Component, OnInit } from '@angular/core';
import { Employee } from '../employees/employees';
import { EmployeeService } from '../employees/employees.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-employee-add',
  templateUrl: './employee-add.component.html',
  styleUrls: ['./employee-add.component.scss']
})
export class EmployeeAddComponent implements OnInit {

  employee: Employee = {
    firstName: '',
    lastName: '',
    age: null,
    birth: '',
    employeeId: null,
    employmentDate: '',
    department: '',
    salary: null,
    email: ''
  }

  successMessage: string = "";

  constructor(private employeeService: EmployeeService) {}

  ngOnInit(): void {
      
  }

  addEmployee(employeeForm: NgForm) {
    console.log("Help me")
    this.employeeService.addEmployee(this.employee).subscribe((data) => {
      this.successMessage = 'Employee Added to Database.';
      employeeForm.resetForm({
        firstName: '',
        lastName: '',
        age: null,
        birth: '',
        employeeId: null,
        employmentDate: '',
        department: '',
        salary: null,
        email: ''
      })
    })
  }

}
