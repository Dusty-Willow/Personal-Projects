import { Pipe, PipeTransform } from '@angular/core';
import { MyData } from '../my-data';

@Pipe({
  name: 'filter'
})
export class emailFilterPipe implements PipeTransform {

transform(data: MyData[], email: string): MyData[] {
    return data.filter((data) => data.email.includes(email));
}

}
