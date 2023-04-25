import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filtertextparser'
})
export class FiltertextparserPipe implements PipeTransform {

  transform(myInput: string): string[] {
    if (myInput == "" || myInput == null) return []
    var result: string[] = [];
    console.log(myInput.toLowerCase().split(" "));
    result = myInput.toLowerCase().split(" ");
    result.forEach((element) => {element.replace(/_/g, " ")})
    console.log(result)
    return result;
  }

}
