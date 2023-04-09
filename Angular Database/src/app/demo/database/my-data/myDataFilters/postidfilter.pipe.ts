import { Pipe, PipeTransform } from '@angular/core';
import { MyDataTable } from '../my-data';

@Pipe({
  name: 'postfilter'
})
export class postIdFilterPipe implements PipeTransform {

    transform(data: MyDataTable[], postID: number): MyDataTable[] {
      if (postID != null) {
        return data.filter((data) => data.postId == postID);
      } else {
        return data
      }        
    }

}