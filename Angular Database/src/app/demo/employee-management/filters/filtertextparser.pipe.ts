import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filtertextparser'
})
export class FiltertextparserPipe implements PipeTransform {

  transform(myInput: string): string[] {
    if (myInput == "" || myInput == null) return []
    console.log(myInput.toLowerCase().split(" "));
    return myInput.toLowerCase().split(" ");
  }

}
