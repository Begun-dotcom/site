// src/declarations.d.ts
declare module '*.jsx' {
  import { ComponentType } from 'react';
  const component: ComponentType<any>;
  export default component;
}

declare module '*.js' {
  import { ComponentType } from 'react';
  const component: ComponentType<any>;
  export default component;
}