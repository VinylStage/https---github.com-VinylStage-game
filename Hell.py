import random
import os

# 캐릭터기본스탯


class Character:
    def __init__(self, name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst):
        self.name = name

        # 소모용
        self.hp = hp  # 체력
        self.mp = mp  # 마나
        self.eng = eng  # 기력
        self.blf = blf  # 믿음/Holy Knight의 마나역할

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.fth = fth  # 신앙력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력
        self.rst = rst  # 기력재생력
        self.rem = rem  # 마나재생력

        self.skills = []

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                choice = int(input()) - 1
                if 0 <= choice < len(self.skills):
                    # 선택한 스킬의 함수 객체 가져오기
                    selected_skill = self.skills[choice]
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# 소드마스터
        # 소마 평타

    def swordman_attack(self, target):
        os.system('cls')
        if random.random() < self.agi:
            return
        damage = self.atk + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}에게 {damage}만큼 칼로 찔렀다.')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

    # 소용돌이

    def whirlwind(self, target):
        os.system('cls')
        if random.random() < target.agi:
            return
        damage = self.atk*0.8
        damage -= target.def_*0.2
        if damage < 0:
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}은 {damage}만큼 망가졌다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}, 소용돌이로 가루가 되었다.')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

    # 머리찢기

    def tearoffhead(self, target):
        os.system('cls')
        if random.random() < target.agi:
            return
        damage = self.atk*1.2
        damage -= target.def_*0.2
        if damage < 0:
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}에게 {damage}만큼 머리가 찢어졌다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}의 머리가 사라졌다!')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

    # 기합

    def spirited(self, target):
        os.system('cls')
        target.def_ -= 20
        self.def_ += 30
        self.hp += 50
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        print(f'{target.name}은(는) 겁에질려 방어력이 20 떨어지고',
              f'{self.name}은(는) 방어력이 30 오르고 50 체력을 회복했다!', sep='\n')
        if target.def_ <= 0:
            print(f'{target.name}이(가) 겁에질려 그대로 쓰러졌다!')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')


# 성기사
        # 성기사 평타

    def holy_attack(self, target):
        os.system('cls')
        if random.random() < target.agi:
            return
        damage = self.atk + self.fth*0.2 + \
            random.randint(-20, 150)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}에게 {damage}만큼 입혔다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}이 성스러워졌다!')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 신성한불꽃

    def sacredfire(self, target):
        os.system('cls')
        if self.blf <= 0:
            print('믿음이 부족하여 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.fth*0.7
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'대충{target.name}에게 {damage}만큼 뜨끈뜨끈해졌다!')
        self.blf -= 30
        print(f'스킬사용으로 믿음이 30 소모 : {self.blf}')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}, 귀중한 단백질원이 되었다')
            self.blf -= 30
            print(f'스킬사용으로 믿음이 30 소모, 남은 믿음 : {self.blf}')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 신성한 빛줄기

    def holyvolt(self, target):
        os.system('cls')
        if self.blf <= 0:
            print('믿음이 부족하여 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.fth
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}에게 {damage}빛을 보게했다!')
        self.blf -= 30
        print(f'스킬사용으로 믿음이 10 소모, 남은 믿음 : {self.blf}')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}아 제발 밖에좀 나가서', '\n', '햇빛도 좀 보고 잔디도 만지고 좀 그래!')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 기도

    def pray(self, target):
        os.system('cls')
        if self.blf <= 0:
            print('믿음이 부족하여 일반공격으로 대체합니다')
            return
        effect = self.fth*0.3
        self.hp += effect
        self.blf += effect*0.5
        print(f'체력을 {effect}만큼 회복하고 믿음을 {effect*0.5}만큼 회복했다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')


# 원소술사
        # 원소술사 평타

    def sorceress_attack(self, target):
        os.system('cls')
        if random.random() < target.agi:
            return
        damage = self.atk + self.int_*0.1 + \
            random.randint(-50, 20)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'대충{target.name}에게 {damage}만큼 톡!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.',
              f'현재마나 : {self.mp}', sep='\n')
        if target.hp <= 0:
            print('너는 뭘해도 죽을놈이구나')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem*1.5
            print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.mp}', sep='\n')

        # 구멍속불

    def fireinthehole(self, target):
        os.system('cls')
        if self.mp <= 0:
            print('마나가 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.int_*0.6
        damage -= target.rep*0.2*0.2  # 방어력으로 물리공격 상쇄
        self.mp -= 20
        print('20마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}자식 {damage}만큼 익었다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.',
              f'현재마나 : {self.mp}', sep='\n')
        if target.hp <= 0:
            print(f'{target.name}, 맛있는 냄새가 솔솔 피어오른다.')
            self.mp -= 20
            print(f'20마나 사용 : {self.mp}')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem
            print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.mp}', sep='\n')

        # 얼음숨결

    def icebreath(self, target):
        os.system('cls')
        if self.mp <= 0:
            print('마나가 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.int_*0.5
        damage -= target.rep*0.2  # 방어력으로 물리공격 상쇄
        self.mp -= 25
        print('25마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}놈 얼리고 {damage}를 입었다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.',
              f'현재마나 : {self.mp}', sep='\n')
        if target.hp <= 0:
            print(f'{target.name}, 선채로 사망..!')
            self.mp -= 25
            print(f'25마나 사용 : {self.mp}')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem
            print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.mp}', sep='\n')

        # 묻어버리기

    def dirtgrave(self, target):
        os.system('cls')
        if self.mp <= 0:
            print('마나가 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.int_*0.8
        damage -= target.def_*0.2*0.2  # 방어력으로 물리공격 상쇄
        self.mp -= 30
        print('30마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}녀석 {damage}피해를 입고 겨우 흙더미에서 나왔다')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.',
              f'현재마나 : {self.mp}', sep='\n')
        if target.hp <= 0:
            print(f'{target.name}, 생 매 장 ~')
            self.mp -= 30
            print(f'30마나 사용 : {self.mp}')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem
            print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.mp}', sep='\n')

        # 회복

    def healself(self, target):
        os.system('cls')
        if self.mp <= 0:
            print('마나가 부족하여 하찮은 일반공격으로 대체합니다')
            return
        self.hp += self.int_*0.3
        print(f'내 체력이 {self.int_*0.3}만큼 회복되었다.')
        self.mp -= 50
        print('50마나 사용')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.',
              f'현재마나 : {self.mp}', sep='\n')


# 인파이터
        # 인파 평타

    def infighter_attack(self, target):
        os.system('cls')
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(-50, 200)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{damage} 톡!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.eng += self.rst
        print(f'{self.name}은(는) {self.rst}만큼 기력을 회복했다.',
              f'현재 기력: {self.eng}', sep='\n')
        if target.hp <= 0:
            print(f'톡 쳤더니 죽어버린 {target.name} 코이츠 wwwww')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*1.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.eng}', sep='\n')

        # 진심펀치

    def sincerepunch(self, target):
        os.system('cls')
        if self.eng <= 0:
            print('기력 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.atk*0.7
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        target.def_ = target.def_ - self.atk*0.3
        self.eng -= 50
        print('50 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{damage}만큼 맞고 {self.atk*0.3}만큼 방어력을 깎았다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.eng += self.rst
        print(f'{self.name}은(는) {self.rst}만큼 기력을 회복했다.',
              f'현재 기력: {self.eng}', sep='\n')
        if target.def_ <= 0:
            target.hp -= 10000
            print(f'{target.name}녀석 방어구가 부서지고 쓰러졌어!')
            self.eng += self.rst*1.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.eng}')

        elif target.hp <= 0:
            print(f'{target.name}, DOWN! {target.name}, DOWN!')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*1.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.eng}', sep='\n')

        # 회전차기

    def whirlkick(self, target):
        os.system('cls')
        if self.eng <= 0:
            print('기력 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.atk*1.2
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        self.eng -= 30
        print('30 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{damage}만큼 아픈 주먹!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.eng += self.rst
        print(f'{self.name}은(는) {self.rst}만큼 기력을 회복했다.',
              f'현재 기력: {self.eng}', sep='\n')
        if target.hp <= 0:
            print(f'{target.name}이 대충 죽었다는 내용')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*1.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.eng}', sep='\n')

        # 엎어치기

    def overthrow(self, target):
        os.system('cls')
        if self.eng <= 0:
            print('기력 부족하여 하찮은 일반공격으로 대체합니다')
            return
        damage = self.atk*1.8
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        self.eng -= 60
        print('60 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{damage}만큼 바닥도 부서졌다!')
        self.hp += self.vit
        print(f'{self.name}은(는) {self.vit}만큼 체력을 회복했다.')
        self.eng += self.rst
        print(f'{self.name}은(는) {self.rst}만큼 기력을 회복했다.',
              f'현재 기력: {self.eng}', sep='\n')
        if target.hp <= 0:
            print(f'{target.name}녀석 바닥에 파묻힌채로 가버렸군')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*1.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.eng}', sep='\n')


# 몬스터 기본스탯
class Monster:
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        self.name = name

        # 소모용
        self.max_HP = hp  # 최대체력
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro
        self.skills = []
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.skills[0](target)
            self.attack_count += 1
        else:
            self.skills[1](target)
            self.attack_count = 0

# Skeleton
        # 스켈레톤 평타

    def skeleton_attack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(-50, 70)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'Skeleton의 일반공격으로 {damage}만큼 데미지를 입었다!')
        if target.hp <= 0:
            print(f'Skeleton의 일반공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 화살

    def arrow(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        target.def_ -= 20
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'Skeleton의 화살로 {damage} 피해를 입고 방어력이 20 떨어졌다!',
              f'현재 방어력 : {target.def_}', '\n')
        if target.hp <= 0:
            print(f'Skeleton의 화살로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')


# Giant Fly
        # 거대파리 평타

    def giantfly_attack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'거대파리의 싸대기로 {damage}만큼 피해를 입었다!')
        if target.hp <= 0:
            print(f'거대파리의 싸대기로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 박치기

    def headattack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + 30
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'거대파리의 박치기 공격으로 {damage}만큼 피해를 입었다!')
        if target.hp <= 0:
            print(f'거대파리의 박치기 공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')


# Beelzebub
        # 베엘제붑 평타


    def beelzebub_attack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(50, 130)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'베엘제붑의 지건으로 {damage}만큼 피해를 입었다!')
        if target.hp <= 0:
            print(f'베엘제붑의 지건으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 벌레공격

    def bugsattack(self, target):
        damage = self.int_*1.5
        damage -= target.rep*0.2  # 마법저항력으로 물리공격 상쇄
        target.hp -= damage
        target.rep -= self.int_*0.2
        self.hp -= self.int_*0.1
        print(f'베엘제붑은 자신의 살점을 때어 벌레공격으로 {damage}만큼 피해를 입고 마법저항력이 {self.int_*0.2} 떨어졌다!',
              f'현재 마법저항력 : {target.rep}', '\n')
        if target.hp <= 0:
            print(f'베엘제붑의 벌레공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('코이츠 구더기밥이 되어버린 wwww')


# Spider
        # 거미 평타


    def spider_attack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(0, 80)  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'거미에게 물려 {damage}만큼 피해를 입었다!')
        if target.hp <= 0:
            print(f'거미에게 물려 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 거미줄 공격

    def webattack(self, target):
        if random.random() < target.agi:
            return
        damage = self.int_*1.2
        damage -= target.rep*0.2
        target.rep -= self.int_*0.1
        if damage < 0:
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'거미줄 공격으로 {damage}만큼 피해를 입고 마법저항력이 {self.int_*0.1} 떨어졌다!',
              f'현재 마법저항력 : {target.rep}', '\n')
        if target.hp <= 0:
            print(f'거미줄 공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')


# Adam's Apple Snake
        # 뱀 평타


    def snakeattack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk + random.randint(0, 80)
        damage -= target.def_*0.2
        if damage < 0:
            damage = 0
            print(f'{self.name} : 오소이')
        target.hp -= damage
        print(f'뱀한테 뺨맞고 {damage}만큼 피해를 입었다!')
        if target.hp <= 0:
            print(f'뱀한테 뺨맞고 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 침뱉기

    def spitting(self, target):
        damage = self.int_*1.2
        damage -= target.rep*0.2
        target.rep -= self.int_*0.1
        print(f'선악과뱀에게 침을 맞고 {damage}만큼 피해를 입고 마법저항력이 {self.int_*0.1} 떨어졌다!',
              f'현재 마법저항력 : {target.rep}', '\n')
        if target.hp <= 0:
            print(f'선악과뱀에게 침을 맞고 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print(f'{target.name}, 이 곳에 침맞고 잠들다')


# LILITH
        # 짓밟기


    def stompon(self, target):
        damage = self.atk*1.5 + self.int_*2.5
        damage -= target.rep*0.2 - target.def_*0.2
        print(f'성역의 어머니에게 밟혀 {damage}만큼 피해를 입었다. 포상이다!')
        if target.hp <= 0:
            print(f'성역의 어머니에게 밟혀 {damage} 피해를 입고 영웅은 성불했다!', '마망!', sep='\n')
            print('성역의 어머니 LILITH, 이제 그녀를 막을 자는 아무도 없다!')

        # 흡혈

    def lifeabsorption(self, target):
        damage = self.int_*3
        damage -= target.rep*0.2
        self.hp += damage*0.5
        print(f'체력흡수를 당해 {damage}만큼 피해를 입었고,', f'그녀는 {damage*0.5}만큼 체력을 회복했다!')
        if target.hp <= 0:
            print(f'{target.name}녀석... {damage} 피해를 입고 결국 모조리 흡수당하여 흔적조차 남지 않았어')


# 자식클래스
# Sword Master Class
class Sword_Master(Character):
    def __init__(self, name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst):
        super().__init__(name, hp, mp, eng, blf, atk,
                         int_, fth, def_, rep, agi, vit, rem, rst)

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력

        self.skills = [self.swordman_attack,
                       self.whirlwind, self.tearoffhead, self.spirited]

# Holy Knight Clas]


class Holy_Knight(Character):
    def __init__(self, name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst):
        super().__init__(name, hp, mp, eng, blf, atk,
                         int_, fth, def_, rep, agi, vit, rem, rst)

        # 소모용
        self.hp = hp  # 체력
        self.blf = blf  # 믿음/Holy Knight의 마나역할

        # 고정스탯
        self.atk = atk  # 공격력
        self.fth = fth  # 신앙력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력

        self.skills = [self.holy_attack,
                       self.sacredfire, self.holyvolt, self.pray]


# Sorceress Class


class Sorceress(Character):
    def __init__(self, name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst):
        super().__init__(name, hp, mp, eng, blf, atk,
                         int_, fth, def_, rep, agi, vit, rem, rst)

        # 소모용
        self.hp = hp  # 체력
        self.mp = mp  # 마나

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력
        self.rem = rem  # 마나재생력

        self.skills = [self.sorceress_attack,
                       self.fireinthehole, self.icebreath, self.dirtgrave, self.healself]

# Infighter Class


class Infighter(Character):
    def __init__(self, name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst):
        super().__init__(name, hp, mp, eng, blf, atk,
                         int_, fth, def_, rep, agi, vit, rem, rst)

        # 소모용
        self.hp = hp  # 체력
        self.eng = eng  # 기력

        # 고정스탯
        self.atk = atk  # 공격력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력
        self.rst = rst  # 기력재생력

        self.skills = [self.infighter_attack,
                       self.sincerepunch, self.whirlkick, self.overthrow]


# 몬스터 클래스

# Skeleton Class


class Skeleton(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.skeleton_attack, self.arrow]


# Giant Fly


class Giant_Fly(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.giantfly_attack, self.headattack]


# Beelzebub


class Beelzebub(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.beelzebub_attack, self.bugsattack]

# Spider


class Spider(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.spider_attack, self.webattack]


# Adam's Apple Snake


class AAS(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.snakeattack, self.spitting]


# LILITH


class LILITH(Monster):
    def __init__(self, name, hp, atk, int_, def_, rep, agi, intro):
        super().__init__(name, hp, atk, int_, def_, rep, agi, intro)
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력
        self.agi = agi  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.stompon, self.lifeabsorption]


def battle():
    print('대충 세상이 거시기해서 거시기해졌으니 구해야한다는 내용의 나래이션')
    print("당신은 누구인가")
    name = input()
    print("무엇으로 살아가는가 (1: Sword Master, 2: Holy Knight, 3: Sorceress, 4: Infighter):")
    character_choice = int(input())

    # character_list = [

    # ]
# (name, hp, mp, eng, blf, atk, int_, fth, def_, rep, agi, vit, rem, rst)
    if character_choice == 1:
        player = Sword_Master(name, 500, 0, 0, 0, 150, 0,
                              0, 100, 80, 0.1, 10, 0, 0)
        print(player.name, ': 눈도 깜짝 안한다!')
    elif character_choice == 2:
        player = Holy_Knight(name, 480, 0, 0, 0, 90,
                             0, 80, 150, 80, 0.1, 8, 0, 0)
        print(player.name, ': Firs mother is coming')
    elif character_choice == 3:
        player = Sorceress(name, 350, 300, 0, 0, 60, 250,
                           0, 80, 60, 0.2, 10, 15, 0)
        print(player.name, ': 레비오우사 not 레비오사아~')
    elif character_choice == 4:
        player = Infighter(name, 650, 0, 400, 0, 100, 0,
                           0, 110, 110, 0.2, 30, 0, 10)
        print(player.name, ': 나는 최강이다')
    else:
        print("입력좀 제대로 해봐", '자 다음!', sep='\n')
        battle()

    # 몬스터 생성
# (name, hp, atk, int_, def_, rep, agi, intro)
    monsters = [
        Skeleton("Skeleton", 5000, 100, 0, 50, 100, 0.1, '달그락달그락'),
        Giant_Fly("Giant Fly", 130, 70, 0, 60, 120, 0.3, '에ㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔ엥'),
        Beelzebub("Beelzebub", 350, 70, 150, 80, 130, 0.1, '어? 나 아직 밥 안시켰는데'),
        Spider("Spider", 150, 130, 80, 100, 40, 0.1, '쉬이익! 쉬이익!'),
        AAS("Adam's Apple Snake", 180, 130, 50, 60, 80, 0.4, '사과 하나 먹을래?'),
        LILITH("LILITH", 1000, 200, 300, 100, 120, 0.2,
               '최초의 여성, 아담의 첫 번째 부인, 성역의 어머니 LILITH가 모습을 드러냈다!\n"내 아이들아, 족쇄를 벗고... 죄악 속에서 아름답게 거듭나라..."')
    ]

    # 전투 진행

    for monster in monsters:
        print(monster.name, ':', monster.intro)
        print(f'내 앞에서 알짱거리는 {monster.name}, 물리쳐야겠지? 아무래도...')
        while player.hp > 0 and monster.hp > 0:
            print(f"{player.name}: {player.hp}")
            print(f"{monster.name}: {monster.hp}")
            player.attack(monster)
            if monster.hp > 0:
                monster.attack(player)
        if player.hp <= 0:
            print("YOU DIED")
            print('리겜?', '하고싶으면 1번을 입력', sep='\n')
            if int(input()) == 1:
                battle()
            else:
                break
        else:
            os.system('cls')
            print(monster.name.upper(), '\n''GREAT ENEMY FELLED')
            print('================================================================================================''\n')
    if player.hp > 0:
        print("대충 세상을 구해서 잘했다는 내용의 아웃트로")


battle()
