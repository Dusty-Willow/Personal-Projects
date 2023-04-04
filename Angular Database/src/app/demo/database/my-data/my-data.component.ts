import { Component, OnInit } from '@angular/core';
import { MyDataService } from './my-data.service';
import { ActivatedRoute } from '@angular/router';
import { pluck } from 'rxjs';
import { SharedModule } from 'src/app/theme/shared/shared.module';
import { CardModule } from 'src/app/theme/shared/components';

@Component({
  selector: 'app-my-data',
  templateUrl: './my-data.component.html',
  styleUrls: ['./my-data.component.scss']
})
export class MyDataComponent implements OnInit {

  data$ = this.myDataService.getData();

  dataSegment$ = this.activatedRoute.data.pipe(
    pluck('data')
  )

  constructor(private myDataService: MyDataService, private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
      
  }

}
