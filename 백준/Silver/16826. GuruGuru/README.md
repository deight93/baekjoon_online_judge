# [Silver III] GuruGuru - 16826 

[문제 링크](https://www.acmicpc.net/problem/16826) 

### 성능 요약

메모리: 30864 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>You are playing a game called <em>Guru Guru Gururin</em>. In this game, you can move with the vehicle called Gururin. There are two commands you can give to Gururin: <code>R</code> and <code>L</code>. When <code>R</code> is sent, Gururin rotates clockwise by 90 degrees. Otherwise, when <code>L</code> is sent, Gururin rotates counterclockwise by 90 degrees.</p>

<p>During the game, you noticed that Gururin obtains magical power by performing special commands. In short, Gururin obtains magical power every time when it performs one round in the clockwise direction from north to north. In more detail, the conditions under which magical power can be obtained is as follows.</p>

<ul>
	<li>At the beginning of the special commands, Gururin faces north.</li>
	<li>At the end of special commands, Gururin faces north.</li>
	<li>Except for the beginning and the end of special commands, Gururin does not face north.</li>
	<li>During the special commands, Gururin faces north, east, south, and west one or more times, respectively, after the command of <code>R</code>.</li>
</ul>

<p>At the beginning of the game, Gururin faces north. For example, if the sequence of commands Gururin received in order is <code>RRRR</code> or <code>RRLRRLRR</code>, Gururin can obtain magical power. Otherwise, if the sequence of commands is <code>LLLL</code> or <code>RLLR</code>, Gururin cannot obtain magical power.</p>

<p>Your task is to calculate how many times Gururin obtained magical power throughout the game. In other words, given the sequence of the commands Gururin received, calculate how many special commands exists in it.</p>

### 입력 

 <p>The input consists of a single test case in the format below.</p>

<pre class="mathjax">$S$</pre>

<p>The first line consists of a string $S$, which represents the sequence of commands Gururin received. S consists of <code>L</code> and <code>R</code>. The length of $S$ is between $1$ and $10^3$ inclusive.</p>

### 출력 

 <p>Print the number of times Gururin obtained magical power throughout the game in one line.</p>

