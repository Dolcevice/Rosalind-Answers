class ToRNA:
    @staticmethod
    def conversion(target):
        dna_to_rna = {'T': 'U'}
        result = ''

        for ch in target:
            try:
                result += dna_to_rna.get(ch)
            except:
                result += ch

        return result
