"""
백준 25758 유전자 조합 (실버1)

1. dict로 첫번째, 두번째 유전자 갯수 정리한 후 
2. 모든 유전자 돌면서 자신보다 작은 반대쪽 유전형질이 있는지 체크
"""
def main():
    input()
    genes = input().split()
    first_gene_dict = {}
    second_gene_dict = {}
    for first_gene, second_gene in genes:
        if first_gene in first_gene_dict:
            first_gene_dict[first_gene] += 1
        else:
            first_gene_dict[first_gene] = 1
        if second_gene in second_gene_dict:
            second_gene_dict[second_gene] += 1
        else:
            second_gene_dict[second_gene] = 1
    possible = set()
    for first_gene, second_gene in genes:
        if len(possible)==26: break
        if first_gene not in possible:
            if second_gene not in second_gene_dict:
                pass
            elif second_gene_dict[second_gene]==1:
                del second_gene_dict[second_gene]
            for key in second_gene_dict:
                if key<=first_gene:
                    possible.add(first_gene)
                    break
            if second_gene not in second_gene_dict:
                second_gene_dict[second_gene] = 1
        if second_gene not in possible:
            if first_gene not in first_gene_dict:
                pass
            elif first_gene_dict[first_gene]==1:
                del first_gene_dict[first_gene]
            for key in first_gene_dict:
                if key<=second_gene:
                    possible.add(second_gene)
                    break
            if first_gene not in first_gene_dict:
                first_gene_dict[first_gene] = 1
    print(len(possible))
    print(*sorted(possible))

main()