import { Component, Input, OnInit } from '@angular/core';
import { Employee } from '../employees/employees';

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {

  @Input() myEmployees : Employee[] = [];
  @Input() multiFilter : string | null;

  constructor() {}

  ngOnInit(): void {
      
  }

}
