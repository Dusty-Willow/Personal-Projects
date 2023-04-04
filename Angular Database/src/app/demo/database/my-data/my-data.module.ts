import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MyDataRoutingModule } from './my-data-routing.module';
import { MyDataComponent } from './my-data.component';
import { HttpClientModule } from '@angular/common/http';
import { CardModule } from 'src/app/theme/shared/components';
import { TablesModule } from '../../pages/tables/tables.module';
import { NgbAccordionModule } from '@ng-bootstrap/ng-bootstrap';
// import {MatExpansionModule} from '@angular/material/expansion';

@NgModule({
  declarations: [
    MyDataComponent
  ],
  imports: [
    CommonModule,
    MyDataRoutingModule,
    HttpClientModule,
    CardModule,
    TablesModule,
    NgbAccordionModule
    // MatExpansionModule,
  ]
})
export class MyDataModule { }
