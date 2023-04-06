import { postFilterPipe } from './postfilter.pipe';

describe('postFilterPipe', () => {
    it('create an instance', () => {
      const pipe = new postFilterPipe();
      expect(pipe).toBeTruthy();
    });
  });