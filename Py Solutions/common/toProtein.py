from common.components import References as ref


class ToProtein:
    @staticmethod
    def conversion(target):
        translated = ''

        count = 0
        insertion = ''

        for ch in target:
            insertion += ch
            count += 1
            if count == 3:
                try:
                    yeet = ref.codon_reference.get(insertion)
                    if yeet == "Stop":
                        translated += ''
                    else:
                        translated += yeet
                    count = 0
                    insertion = ''
                except:
                    print("unknown ref")
                    break

        return translated
