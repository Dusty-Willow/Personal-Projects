import { Pipe, PipeTransform } from '@angular/core';
import { MyData } from '../my-data';

@Pipe({
  name: 'filter'
})
export class postFilterPipe implements PipeTransform {

    transform(data: MyData[], postID: string): MyData[] {
        return data.filter((data) => data.postId.toString().includes(postID));
      }

}