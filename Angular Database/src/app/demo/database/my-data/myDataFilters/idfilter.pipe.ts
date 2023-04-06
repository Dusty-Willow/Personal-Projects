import { Pipe, PipeTransform } from '@angular/core';
import { MyData } from '../my-data';

@Pipe({
  name: 'filter'
})
export class idFilterPipe implements PipeTransform {

  transform(data: MyData[], id: string): MyData[] {
    return data.filter((data) => data.id.toString().includes(id));
  }

}