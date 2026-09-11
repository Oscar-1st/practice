function findDoublers(str) {
  str = str.toLowerCase();

  for (let i = 0; i < str.length; i++) {
    if (str.indexOf(str[i]) !== i) {
      return true;
    }
  }

  return false;
}
const result = findDoublers("hello");
console.log(result);


// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function getReverse(rev) {
//   let result = rev.split("").reverse().join("");
//   console.log(result);
// }
// getReverse("hello");
// getReverse("ogabek");
// getReverse("Assalomu alekum");
// getReverse("omadbek");

// TASK E: 

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"