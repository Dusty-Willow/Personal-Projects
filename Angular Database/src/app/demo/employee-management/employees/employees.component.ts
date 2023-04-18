import { Component, Input, OnInit } from '@angular/core';
import { Employee } from './employees';
import { EmployeeService } from './employees.service';
import { ActivatedRoute } from '@angular/router';
import { Subject, catchError, of } from 'rxjs';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.scss']
})
export class EmployeesComponent implements OnInit {

  employees: Employee[] = [] 

  error$ = new Subject<string>()

  employeeData$ = this.myEmployeeService.getEmployees$.pipe(
    catchError((err) => {
      console.log(err);
      this.error$.next(err.message);
      return of([])
    })
  )

  currentPage: number = 1
  entriesDisplayed: number;
  // totalEntries: number = this.employeeData$;

  onSelected(value : string): void {
    this.entriesDisplayed = parseInt(value);
    console.log(this.entriesDisplayed)
  }

  changePage(page: number): void {
    this.currentPage = page;
  }

  multiFilter = new FormControl(null);

  constructor(private myEmployeeService: EmployeeService, private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
    
  }
}
