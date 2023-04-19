import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { Employee } from '../employees/employees';
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

  constructor() {}

  ngOnInit(): void {
      
  }

  key = 'id';
  reverse : boolean = false;
  sort(key) {
    this.key = key;
    this.reverse = !this.reverse;
  }

}
