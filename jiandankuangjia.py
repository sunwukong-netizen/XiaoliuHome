# This file is created by opstool.tcl2py(), author:: Yexiang Yan
import opstool as opst
import openseespy.opensees as ops
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ops.wipe()
ops.model('basic', '-ndm', 3, '-ndf', 6)
ops.node(1, 0, 0, 3000)
ops.node(2, 3000, 0, 3000)
ops.node(3, 0, 0, 0)
ops.node(4, 3000, 0, 0)
ops.node(5, 3000, 0, 6000)
ops.node(6, 0, 0, 6000)
ops.node(7, -3000, 0, 3000)
ops.node(8, -3000, 0, 0)
ops.node(9, -3000, 0, 6000)
ops.fix(8, 1, 1, 1, 1, 1, 1)
ops.fix(3, 1, 1, 1, 1, 1, 1)
ops.fix(4, 1, 1, 1, 1, 1, 1)
ops.uniaxialMaterial('Steel01', 1, 235.0, 200000.0, 0.01)
ops.section('Fiber', 2, '-GJ', 10000.0)
ops.fiber(-90.0, -90.0, 400.0, 1)
ops.fiber(-70.0, -90.0, 400.0000000000003, 1)
ops.fiber(-50.0, -90.0, 400.0, 1)
ops.fiber(-30.000000000000004, -90.0, 400.0, 1)
ops.fiber(-10.000000000000002, -90.0, 400.0, 1)
ops.fiber(9.999999999999996, -90.0, 399.99999999999994, 1)
ops.fiber(29.99999999999999, -90.0, 400.0000000000001, 1)
ops.fiber(50.0, -90.0, 400.0000000000003, 1)
ops.fiber(70.0, -90.0, 400.0000000000003, 1)
ops.fiber(90.0, -90.0, 400.0, 1)
ops.fiber(-90.0, -70.0, 400.0000000000003, 1)
ops.fiber(-70.0, -70.0, 400.0000000000003, 1)
ops.fiber(-50.0, -70.0, 399.99999999999955, 1)
ops.fiber(-30.000000000000004, -70.0, 400.0, 1)
ops.fiber(-10.000000000000002, -70.0, 400.0, 1)
ops.fiber(9.999999999999998, -70.0, 400.0, 1)
ops.fiber(29.99999999999999, -70.0, 399.99999999999966, 1)
ops.fiber(49.999999999999986, -69.99999999999999, 399.9999999999999, 1)
ops.fiber(70.0, -70.0, 400.0000000000003, 1)
ops.fiber(90.0, -70.0, 400.0000000000003, 1)
ops.fiber(-90.0, -50.0, 400.0, 1)
ops.fiber(-70.0, -49.99999999999999, 399.99999999999955, 1)
ops.fiber(-50.0, -50.0, 399.99999999999955, 1)
ops.fiber(-30.000000000000004, -50.0, 400.0000000000001, 1)
ops.fiber(-10.000000000000002, -50.0, 400.0, 1)
ops.fiber(9.999999999999998, -50.0, 399.99999999999994, 1)
ops.fiber(29.99999999999999, -50.0, 399.99999999999966, 1)
ops.fiber(49.99999999999999, -50.0, 399.9999999999997, 1)
ops.fiber(70.0, -50.0, 399.99999999999955, 1)
ops.fiber(90.0, -50.0, 400.0, 1)
ops.fiber(-90.0, -30.0, 400.0, 1)
ops.fiber(-70.0, -30.0, 400.0, 1)
ops.fiber(-50.0, -30.000000000000004, 400.0000000000001, 1)
ops.fiber(-30.000000000000004, -30.0, 400.0000000000001, 1)
ops.fiber(-10.000000000000002, -30.0, 400.0, 1)
ops.fiber(9.999999999999995, -30.0, 400.0, 1)
ops.fiber(29.99999999999999, -30.000000000000004, 400.0000000000001, 1)
ops.fiber(50.0, -30.000000000000007, 400.00000000000045, 1)
ops.fiber(70.0, -30.000000000000004, 400.0000000000001, 1)
ops.fiber(90.0, -30.0, 400.0, 1)
ops.fiber(-90.0, -10.000000000000002, 400.0, 1)
ops.fiber(-70.0, -10.000000000000002, 400.0, 1)
ops.fiber(-50.0, -10.000000000000002, 400.0, 1)
ops.fiber(-30.000000000000004, -10.000000000000002, 400.0, 1)
ops.fiber(-10.000000000000002, -10.000000000000002, 400.0, 1)
ops.fiber(9.999999999999996, -10.000000000000002, 399.99999999999994, 1)
ops.fiber(29.99999999999999, -10.000000000000002, 399.99999999999983, 1)
ops.fiber(50.0, -10.000000000000002, 400.0000000000002, 1)
ops.fiber(70.0, -10.000000000000002, 400.0, 1)
ops.fiber(90.0, -10.000000000000002, 400.0, 1)
ops.fiber(-90.0, 9.999999999999996, 399.99999999999994, 1)
ops.fiber(-70.0, 9.999999999999998, 400.0, 1)
ops.fiber(-50.0, 9.999999999999998, 400.0, 1)
ops.fiber(-30.000000000000004, 9.999999999999996, 400.0, 1)
ops.fiber(-10.000000000000002, 9.999999999999996, 399.99999999999994, 1)
ops.fiber(9.999999999999998, 9.999999999999998, 400.0, 1)
ops.fiber(29.999999999999993, 9.999999999999998, 399.9999999999999, 1)
ops.fiber(50.0, 9.999999999999998, 400.0000000000001, 1)
ops.fiber(70.0, 9.999999999999996, 399.99999999999994, 1)
ops.fiber(90.0, 9.999999999999996, 399.99999999999994, 1)
ops.fiber(-90.0, 29.999999999999993, 400.0000000000001, 1)
ops.fiber(-70.0, 29.999999999999993, 399.99999999999966, 1)
ops.fiber(-50.0, 29.999999999999996, 399.99999999999966, 1)
ops.fiber(-30.000000000000004, 29.999999999999993, 400.0, 1)
ops.fiber(-10.000000000000002, 29.999999999999996, 399.9999999999999, 1)
ops.fiber(9.999999999999998, 30.0, 400.0, 1)
ops.fiber(29.99999999999999, 29.999999999999993, 399.9999999999996, 1)
ops.fiber(50.0, 29.999999999999993, 399.9999999999999, 1)
ops.fiber(70.0, 29.99999999999999, 399.99999999999966, 1)
ops.fiber(90.0, 29.999999999999996, 400.0000000000001, 1)
ops.fiber(-90.0, 49.99999999999999, 400.0000000000003, 1)
ops.fiber(-70.0, 49.999999999999986, 399.9999999999999, 1)
ops.fiber(-50.0, 49.999999999999986, 399.9999999999997, 1)
ops.fiber(-30.000000000000007, 49.99999999999999, 400.00000000000045, 1)
ops.fiber(-10.000000000000002, 50.0, 400.0000000000001, 1)
ops.fiber(9.999999999999998, 50.0, 400.0000000000001, 1)
ops.fiber(29.99999999999999, 49.999999999999986, 399.9999999999999, 1)
ops.fiber(49.99999999999999, 49.999999999999986, 400.00000000000006, 1)
ops.fiber(70.0, 49.999999999999986, 399.9999999999999, 1)
ops.fiber(90.0, 50.0, 400.0000000000003, 1)
ops.fiber(-90.0, 70.0, 400.0000000000003, 1)
ops.fiber(-69.99999999999999, 69.99999999999999, 400.0000000000003, 1)
ops.fiber(-50.0, 70.0, 399.99999999999955, 1)
ops.fiber(-30.000000000000007, 70.0, 400.0000000000001, 1)
ops.fiber(-10.000000000000004, 70.0, 400.0, 1)
ops.fiber(9.999999999999996, 70.0, 399.99999999999994, 1)
ops.fiber(29.99999999999999, 70.0, 399.9999999999999, 1)
ops.fiber(49.999999999999986, 69.99999999999999, 399.99999999999994, 1)
ops.fiber(69.99999999999999, 69.99999999999999, 400.0000000000003, 1)
ops.fiber(90.0, 70.0, 400.0000000000003, 1)
ops.fiber(-90.0, 90.0, 400.0, 1)
ops.fiber(-70.0, 90.0, 400.0000000000003, 1)
ops.fiber(-50.0, 90.0, 400.0, 1)
ops.fiber(-30.000000000000004, 90.0, 400.0, 1)
ops.fiber(-10.000000000000002, 90.0, 400.0, 1)
ops.fiber(9.999999999999996, 90.0, 399.99999999999994, 1)
ops.fiber(29.99999999999999, 90.0, 400.0000000000001, 1)
ops.fiber(49.99999999999999, 90.0, 400.0000000000003, 1)
ops.fiber(70.0, 90.0, 400.0000000000003, 1)
ops.fiber(90.0, 90.0, 400.0, 1)
ops.geomTransf('Linear', 1, 0.0, 0.0, 1.0)
ops.beamIntegration('Lobatto', 1, *[2, 5])
ops.element('forceBeamColumn', 1, 1, 2, 1, 1)
ops.geomTransf('Linear', 2, 1.0, 0.0, -0.0)
ops.beamIntegration('Lobatto', 2, *[2, 5])
ops.element('forceBeamColumn', 2, 3, 1, 2, 2)
ops.geomTransf('Linear', 3, -1.0, 0.0, 0.0)
ops.beamIntegration('Lobatto', 3, *[2, 5])
ops.element('forceBeamColumn', 3, 2, 4, 3, 3)
ops.geomTransf('Linear', 4, 1.0, 0.0, -0.0)
ops.beamIntegration('Lobatto', 4, *[2, 5])
ops.element('forceBeamColumn', 4, 2, 5, 4, 4)
ops.geomTransf('Linear', 5, 1.0, 0.0, -0.0)
ops.beamIntegration('Lobatto', 5, *[2, 5])
ops.element('forceBeamColumn', 5, 1, 6, 5, 5)
ops.geomTransf('Linear', 6, 0.0, 0.0, 1.0)
ops.beamIntegration('Lobatto', 6, *[2, 5])
ops.element('forceBeamColumn', 6, 7, 1, 6, 6)
ops.geomTransf('Linear', 7, 1.0, 0.0, -0.0)
ops.beamIntegration('Lobatto', 7, *[2, 5])
ops.element('forceBeamColumn', 7, 8, 7, 7, 7)
ops.geomTransf('Linear', 8, 0.0, 0.0, 1.0)
ops.beamIntegration('Lobatto', 8, *[2, 5])
ops.element('forceBeamColumn', 8, 9, 6, 8, 8)
ops.geomTransf('Linear', 9, 0.0, 0.0, 1.0)
ops.beamIntegration('Lobatto', 9, *[2, 5])
ops.element('forceBeamColumn', 9, 6, 5, 9, 9)
ops.geomTransf('Linear', 10, 1.0, 0.0, -0.0)
ops.beamIntegration('Lobatto', 10, *[2, 5])
ops.element('forceBeamColumn', 10, 7, 9, 10, 10)
ops.recorder('Node', '-file', 'node5.out', '-time', '-node', 5, '-dof', 1, 2, 3, 'disp')
ops.timeSeries('Constant', 1)
ops.pattern('Plain', 3, 1)
ops.load(5, 100000000.0, 0.0, 0.0, 0.0, 0.0, 0.0)
ops.load(6, 100000000.0, 0.0, 0.0, 0.0, 0.0, 0.0)
ops.load(9, 100000000.0, 0.0, 0.0, 0.0, 0.0, 0.0)
ops.domainChange()
ops.constraints('Penalty', 1e+18, 1e+18)
ops.numberer('RCM',)
ops.system('UmfPack',)
ops.test('EnergyIncr', 0.0001, 1000)
ops.algorithm('NewtonLineSearch',)
ops.integrator('LoadControl', 0.0)
ops.analysis('Static',)
nodeID = 5  # 指定节点的ID

# 获取节点在X方向的位移
dispX = ops.nodeDisp(nodeID, 1) # 第二个参数为1，表示X方向

# 获取节点在Y方向的位移
dispY = ops.nodeDisp(nodeID, 2) # 第二个参数为2，表示Y方向

# 如果是三维模型，还可以获取Z方向的位移
# dispZ = ops.nodeDisp(nodeID, 3) # 第二个参数为3，表示Z方向

print(f"节点{nodeID}在X方向的位移为: {dispX}")
print(f"节点{nodeID}在Y方向的位移为: {dispY}")
# 如果是三维模型，还可以打印Z方向的位移
# print(f"节点{nodeID}在Z方向的位移为: {dispZ}")
# 如果是三维模型，还可以打印Z方向的位移
dispZ = ops.nodeDisp(nodeID, 3)
print(f"节点{nodeID}在Z方向的位移为: {dispZ}")
""" opst.plot_model()
# 提取节点坐标
nodes = ops.getNodeTags()
node_coords = {node: ops.nodeCoord(node) for node in nodes}

# 创建3D视图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制单元（这里仅示意，根据实际单元类型和连接方式进行绘制）
for elem in ops.getEleTags():
    nodes = ops.eleNodes(elem)
    x = [node_coords[node][0] for node in nodes]
    y = [node_coords[node][1] for node in nodes]
    z = [node_coords[node][2] for node in nodes]
    ax.plot(x, y, z, 'g-')  # 'b-' 表示蓝色实线

# 在节点位置添加编号
for node, coords in node_coords.items():
    ax.text(coords[0], coords[1], coords[2], f'{node}', color='red')
    
# 假设节点1有约束作为示例
# 绘制约束符号，这里简单用红色的星号'*'表示
fixed_nodes = [8,3,4]
fix = fixed_nodes 
for i in fix:
    coords = ops.nodeCoord(i)
    ax.scatter(coords[0], coords[1], coords[2], s=100, c='red', marker='*')
    
# 设置图表标题和轴标签
ax.set_title('框架及节点编号')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图表
plt.show()
 """