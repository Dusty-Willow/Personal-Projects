import { Component, Input, OnInit } from '@angular/core';
import { MyDataService } from '../../my-data.service';
import { ActivatedRoute } from '@angular/router';
import { pluck } from 'rxjs';

@Component({
  selector: 'app-mydatatable',
  templateUrl: './mydatatable.component.html',
  styleUrls: ['./mydatatable.component.scss']
})
export class MydatatableComponent implements OnInit {

  @Input() entryID : string;
  @Input() postID : string;
  @Input() name : string;
  @Input() email : string;

  data$ = this.myDataService.getData();

  dataSegment$ = this.activatedRoute.data.pipe(
    pluck('data')
  )

  constructor(private myDataService: MyDataService, private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
      
  }

}
