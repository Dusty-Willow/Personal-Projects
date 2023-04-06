import { Component, Input, OnInit } from '@angular/core';
import { MyDataService } from './my-data.service';
import { ActivatedRoute } from '@angular/router';
import { FormControl } from '@angular/forms';
import { MydatatableComponent } from './myDataTable/mydatatable/mydatatable.component';
import { catchError, of } from 'rxjs';

@Component({
  selector: 'app-my-data',
  templateUrl: './my-data.component.html',
  styleUrls: ['./my-data.component.scss']
})
export class MyDataComponent implements OnInit {

  idFilter = new FormControl("");
  postFilter = new FormControl("");
  nameFilter = new FormControl("");
  emailFilter = new FormControl("");

  constructor(private myDataService: MyDataService, private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
      
  }

}
