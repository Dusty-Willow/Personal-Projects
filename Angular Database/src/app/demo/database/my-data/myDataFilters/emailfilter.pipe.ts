import { Pipe, PipeTransform } from '@angular/core';
import { MyDataTable } from '../my-data';

@Pipe({
  name: 'emailfilter'
})
export class emailFilterPipe implements PipeTransform {

transform(data: MyDataTable[], email: string): MyDataTable[] {
    if (!(email === "")) {
      return data.filter((data) => (data.email.toLowerCase()).includes(email.toLowerCase()));
    } else {
      return data
    }
}

}
