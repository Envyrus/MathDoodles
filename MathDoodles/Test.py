from vtk import *

vtkDataSet

renWin = vtkRenderWindow() #Container Class for vtkRenderer Objects
renWin.SetSize(600,300)

testData = vtkDataSetAlgorithm()
testData.AddInput()

testObject = vtkDataObject()


ren1 = vtkRenderer()
ren1.SetViewport(0.0,0.0,0.5,1.0)
ren1.SetBackground(0.8,0.4,0.2)
renWin.AddRenderer(ren1)

ren2 = vtkRenderer()
ren2.SetViewport(0.5,0.0,1.0,1.0)
ren2.SetBackground(0.1,0.2,0.4)
renWin.AddRenderer(ren2)

cubeData = vtkCubeSource()
line = vtkPolyLine()


cubeMapper = vtkPolyDataMapper() #Mapper handles a data Object and knows how to render it
cubeMapper.SetInput(cubeData.GetOutput())

cubeActor = vtkActor()
cubeActor.SetMapper(cubeMapper)

ren1.AddActor(cubeActor)
ren1.ResetCamera()

cubeActor.RotateX(30.0)
cubeActor.RotateY(20.0)

cubeActor.GetProperty().SetColor(1.0,0.7,0.7)

iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()

