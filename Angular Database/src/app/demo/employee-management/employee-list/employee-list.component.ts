import { Component, Input, OnInit } from '@angular/core';
import { Employee } from '../employees/employees';
import { EmployeeService } from '../employees/employees.service';
import { EmployeesComponent } from '../employees/employees.component';
// import {MatPaginator, MatSort, MatTableDataSource} from '@angular/material';

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {

  @Input() myEmployees : Employee[] = [];
  @Input() multiFilter : string | null;
  @Input() noOfItems : number = 5;
  page : number = 1;

  // @ViewChild(MatPaginator)

  constructor(private employeeService: EmployeeService, private empComp: EmployeesComponent) {}

  ngOnInit(): void {
      
  }

  key = 'id';
  reverse : boolean = false;
  sort(key) {
    this.key = key;
    this.reverse = !this.reverse;
  }

  delete(emp: Employee) {
    if(confirm("Are you sure you wish to delete this employee?")) {
      this.employeeService.deleteEmployee(emp["Employee ID"]).subscribe();
      this.empComp.reload();
    }
  }

  
}
