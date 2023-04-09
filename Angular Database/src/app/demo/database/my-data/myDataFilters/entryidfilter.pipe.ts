import { Pipe, PipeTransform } from '@angular/core';
import { MyDataTable } from '../my-data';

@Pipe({
  name: 'entryfilter'
})
export class entryIdFilterPipe implements PipeTransform {

  transform(data: MyDataTable[], entryID: number): MyDataTable[] {
    if (entryID != null) {
      return data.filter((data) => data.id == entryID)
    } else {
      return data
    }
  }

}