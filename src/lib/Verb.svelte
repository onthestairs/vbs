<script>
  import Conjugation from "./Conjugation.svelte";

  export let verb;

  const reset = (verbInfinitive) => {
    console.log("infinitive is", verbInfinitive);
    firstPersonSingular = "";
    secondPersonSingular = "";
    thirdPersonSingular = "";
    firstPersonPlural = "";
    secondPersonPlural = "";
    thirdPersonPlural = "";
  };
  $: {
    // reset the answers if the infinitive has changed
    reset(verb.infinitive);
  }

  let firstPersonSingular = "";
  $: firstPersonSingularCorrect =
    firstPersonSingular === verb.indicative.present.first_person_singular;
  $: if (firstPersonSingularCorrect) {
    secondPersonSingularInput.focus();
  }

  let secondPersonSingularInput;
  let secondPersonSingular = "";
  $: secondPersonSingularCorrect =
    secondPersonSingular === verb.indicative.present.second_person_singular;
  $: if (secondPersonSingularCorrect) {
    thirdPersonSingularInput.focus();
  }

  let thirdPersonSingularInput;
  let thirdPersonSingular = "";
  $: thirdPersonSingularCorrect =
    thirdPersonSingular === verb.indicative.present.third_person_singular;
  $: if (thirdPersonSingularCorrect) {
    firstPersonPluralInput.focus();
  }

  let firstPersonPluralInput;
  let firstPersonPlural = "";
  $: firstPersonPluralCorrect =
    firstPersonPlural === verb.indicative.present.first_person_plural;
  $: if (firstPersonPluralCorrect) {
    secondPersonPluralInput.focus();
  }

  let secondPersonPluralInput;
  let secondPersonPlural = "";
  $: secondPersonPluralCorrect =
    secondPersonPlural === verb.indicative.present.second_person_plural;
  $: if (secondPersonPluralCorrect) {
    thirdPersonPluralInput.focus();
  }

  let thirdPersonPluralInput;
  let thirdPersonPlural = "";
  $: thirdPersonPluralCorrect =
    thirdPersonPlural === verb.indicative.present.third_person_plural;
</script>

<h1 class="mb-8 text-center text-5xl font-bold italic underline">
  {verb.infinitive}
</h1>

<div class="flex flex-col text-3xl">
  <Conjugation
    pronoun="Je"
    bind:value={firstPersonSingular}
    isCorrect={firstPersonSingularCorrect}
  />
  <Conjugation
    pronoun="Tu"
    bind:value={secondPersonSingular}
    isCorrect={secondPersonSingularCorrect}
    bind:inputRef={secondPersonSingularInput}
  />
  <Conjugation
    pronoun="Il/Elle/On"
    bind:value={thirdPersonSingular}
    isCorrect={thirdPersonSingularCorrect}
    bind:inputRef={thirdPersonSingularInput}
  />
  <Conjugation
    pronoun="Nous"
    bind:value={firstPersonPlural}
    isCorrect={firstPersonPluralCorrect}
    bind:inputRef={firstPersonPluralInput}
  />
  <Conjugation
    pronoun="Vous"
    bind:value={secondPersonPlural}
    isCorrect={secondPersonPluralCorrect}
    bind:inputRef={secondPersonPluralInput}
  />
  <Conjugation
    pronoun="Ils/Elles"
    bind:value={thirdPersonPlural}
    isCorrect={thirdPersonPluralCorrect}
    bind:inputRef={thirdPersonPluralInput}
  />
</div>
