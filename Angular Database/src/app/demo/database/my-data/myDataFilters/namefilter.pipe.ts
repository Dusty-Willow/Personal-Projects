import { Pipe, PipeTransform } from '@angular/core';
import { MyData } from '../my-data';

@Pipe({
  name: 'filter'
})
export class nameFilterPipe implements PipeTransform {

    transform(data: MyData[], name: string): MyData[] {
      return data.filter((data) => data.name.includes(name));
    }
  
  }