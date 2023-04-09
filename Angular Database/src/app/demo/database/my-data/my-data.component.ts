import { Component, Input, OnInit } from '@angular/core';
import { MyDataService } from './my-data.service';
import { ActivatedRoute } from '@angular/router';
import { FormControl } from '@angular/forms';
import { Subject, catchError, of } from 'rxjs';
import { MyDataTable } from './my-data';

@Component({
  selector: 'app-my-data',
  templateUrl: './my-data.component.html',
  styleUrls: ['./my-data.component.scss']
})
export class MyDataComponent implements OnInit {

  dataTable : MyDataTable[] = [];

  error$ = new Subject<string>();

  data$ = this.myDataService.getData$.pipe(
    catchError((err) => {
      console.log(err);
      this.error$.next(err.message);
      return of([]);
    })
  );

  entryIdFilter = new FormControl(null);
  postIdFilter = new FormControl(null);
  nameFilter = new FormControl("");
  emailFilter = new FormControl("");

  constructor(private myDataService: MyDataService, private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
      
  }

}
