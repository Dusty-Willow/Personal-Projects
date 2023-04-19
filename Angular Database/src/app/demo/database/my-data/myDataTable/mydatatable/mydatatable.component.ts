import { Component, Input, OnInit } from '@angular/core';
import { MyDataTable } from '../../my-data';

@Component({
  selector: 'app-mydatatable',
  templateUrl: './mydatatable.component.html',
  styleUrls: ['./mydatatable.component.scss']
})
export class MydatatableComponent implements OnInit {

  @Input() myData : MyDataTable[] = [];
  @Input() entryID : number | null;
  @Input() postID : number | null;
  @Input() name : string;
  @Input() email : string;

  @Input() noOfItems: number = 5;
  page : number = 1;

  constructor() {}

  ngOnInit(): void {
      
  }

}
