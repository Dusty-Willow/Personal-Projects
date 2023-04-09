import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MyDataRoutingModule } from './my-data-routing.module';
import { MyDataComponent } from './my-data.component';
import { HttpClientModule } from '@angular/common/http';
import { CardModule } from 'src/app/theme/shared/components';
import { TablesModule } from '../../pages/tables/tables.module';
import { NgbAccordionModule } from '@ng-bootstrap/ng-bootstrap';
import { MydatatableComponent } from './myDataTable/mydatatable/mydatatable.component';
import { entryIdFilterPipe } from './myDataFilters/entryidfilter.pipe';
import { postIdFilterPipe } from './myDataFilters/postidfilter.pipe';
import { nameFilterPipe } from './myDataFilters/namefilter.pipe';
import { emailFilterPipe } from './myDataFilters/emailfilter.pipe';
import { ReactiveFormsModule } from '@angular/forms';
// import {MatExpansionModule} from '@angular/material/expansion';

@NgModule({
  declarations: [
    MyDataComponent,
    MydatatableComponent,
    entryIdFilterPipe,
    postIdFilterPipe,
    nameFilterPipe,
    emailFilterPipe

  ],
  imports: [
    CommonModule,
    MyDataRoutingModule,
    HttpClientModule,
    CardModule,
    TablesModule,
    NgbAccordionModule,
    ReactiveFormsModule
    // MatExpansionModule,
  ]
})
export class MyDataModule { }
