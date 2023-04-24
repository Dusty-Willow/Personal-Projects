import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbAccordionModule, NgbDropdown, NgbDropdownItem, NgbDropdownMenu, NgbDropdownToggle } from '@ng-bootstrap/ng-bootstrap';
import { EmployeesComponent } from './employees.component';
import { EmployeeListComponent } from '../employee-list/employee-list.component';
import { EmployeesRoutingModule } from './employees-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { CardModule } from 'src/app/theme/shared/components';
import { TablesModule } from '../../pages/tables/tables.module';
import { ReactiveFormsModule } from '@angular/forms';
import { MultifilterPipe } from '../filters/multifilter.pipe';
import { FiltertextparserPipe } from '../filters/filtertextparser.pipe';
import { PaginationComponent } from '../pagination/pagination.component';
import { Ng2OrderModule } from 'ng2-order-pipe';
import { NgxPaginationModule } from 'ngx-pagination';



@NgModule({
  declarations: [
    EmployeesComponent,
    EmployeeListComponent,
    MultifilterPipe,
    FiltertextparserPipe,
    PaginationComponent
  ],
  imports: [
    CommonModule,
    EmployeesRoutingModule,
    HttpClientModule,
    CardModule,
    TablesModule,
    NgbAccordionModule,
    ReactiveFormsModule,
    Ng2OrderModule,
    NgxPaginationModule,
    NgbDropdown,
    NgbDropdownItem,
    NgbDropdownMenu,
    NgbDropdownToggle
  ]
})
export class EmployeesModule { }
