/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
const twoEditWords=(t,o)=>{let r=[];for(const e of t){let t=!1;for(const r of o)if(can(e,r)){t=!0;break}t&&r.push(e)}return r},can=(t,o)=>{let r=t.length,e=0;for(let n=0;n<r;n++)t[n]!=o[n]&&e++;return e<=2};