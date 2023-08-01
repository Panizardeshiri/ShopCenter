import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filterproducts'
})
export class FilterproductsPipe implements PipeTransform {

  transform(items: any[], searchText: string): any[] {
    // if (!items) return [];
    if (!searchText) return [];

    searchText = searchText.toLowerCase();
    return items.filter((it) => {
      return it.name.toLowerCase().includes(searchText);
    });
  }
}
