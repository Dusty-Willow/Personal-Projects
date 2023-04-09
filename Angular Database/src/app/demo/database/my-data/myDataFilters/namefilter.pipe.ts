import { Pipe, PipeTransform } from '@angular/core';
import { MyDataTable } from '../my-data';

@Pipe({
  name: 'namefilter'
})
export class nameFilterPipe implements PipeTransform {

    transform(data: MyDataTable[], name: string): MyDataTable[] {
      if (!(name === "")) {
        return data.filter((data) => data.name.toString().toLowerCase().includes(name.toLowerCase()));
      } else {
        return data
      }      
    }
  
  }