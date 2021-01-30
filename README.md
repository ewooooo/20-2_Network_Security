# 20-2_Network_Security
2020-2 네트워크보안 Term-Project


## ARP 스푸핑 공격 대응 방법

ARP 스푸핑 공격 발생 시 Victim에 ARP 테이블이 변조되어 중복된 MAC 주소(물리주소)가 생기게 되므로 이를 감지 또는 감지 후 차단.

### 테스트 가상환경 구조
![KakaoTalk_20210130_143622382.png](KakaoTalk_20210130_143622382.png)


### 대응방법

[1] XArp 툴을 이용한 ARP 테이블 지속적 체크
  
    XArp 툴은 ARP 테이블에 중복된 MAC 주소 발생 시 즉시 사용자에게 알림 제공
  
[2] Python 프로그램으로 ARP 테이블 주기적 체크 후 공격감지 시 사용포트 차단
 
    우분투 '/proc/net/arp' ARP 테이블 중복 검사
    공격 발생시 사용 하던 Telnet 23의 process 번호를 조회하여 Telnel을 kill 하여 Telnet 하이재킹 공격을 일시적으로 차단. 
