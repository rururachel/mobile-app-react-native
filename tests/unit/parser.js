// parser.js

import { parse } from 'date-fns';

const parser = (dateString) => {
  const dateFormat = /^\d{4}-\d{2}-\d{2}$/;
  if (!dateString || !dateFormat.test(dateString)) {
    throw new Error('Invalid date string');
  }

  const date = parse(dateString, 'yyyy-MM-dd', new Date());
  return date;
};

export default parser;